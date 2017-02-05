var chatApp = angular.module('chatApp', []);

chatApp.controller('mainController', function($scope, $timeout) {
    $scope.messages = [{time: "2017-02-04T19:10:21.932Z", message: "Hi, how are you?"},
    {time: "2017-02-04T19:12:21.932Z", message: "Good, you?"},
    {time: "2017-02-04T19:14:21.932Z", message: "Good"}];

    $scope.messages2 = [];


    $scope.users = [{name: "Alex", dob: "1995-02-04T19:10:21.93", location: "London, UK", messages: $scope.messages},
    {name: "Jane", dob: "1994-05-07T19:10:21.93", location: "Manchester, UK", messages: $scope.messages2}];

    $scope.currentChatUser = $scope.users[0];

    $scope.post_mess = function() {

        if($scope.myMessage != "") {
            $scope.newPost = {};
            $scope.newPost.time = new Date();
            $scope.newPost.message = $scope.myMessage;

            console.log($scope.newPost);

            $scope.currentChatUser.messages.push($scope.newPost);
            $scope.myMessage = "";
            $.post("http://127.0.0.1:3600", $scope.newPost);
        }

        $timeout($scope.updateScroll, 100);
    }

    $scope.updateScroll = function() {
        var element = document.getElementById("scrollable");
        element.scrollTop = element.scrollHeight;
    }

    $scope.changeChat = function(user) {
        $scope.currentChatUser = user;
    }

});
