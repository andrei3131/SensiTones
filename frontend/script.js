var chatApp = angular.module('chatApp', []);

chatApp.controller('mainController', function($scope, $timeout) {
    $scope.messages = [{user: "", time: "2017-02-04T19:10:21.932Z", message: "Hi, how are you?"},
    {user: "Alex", time: "2017-02-04T19:12:21.932Z", message: "Good, you?"}
    ];

    $scope.messages2 = [];


    $scope.users = [{name: "Alex", dob: "1995-02-04T19:10:21.93", location: "London, UK", messages: $scope.messages},
    {name: "Jane", dob: "1994-05-07T19:10:21.93", location: "Manchester, UK", messages: $scope.messages2}];

    $scope.currentChatUser = $scope.users[0];

    $scope.post_mess = function() {

        if($scope.myMessage != "") {
            $scope.newPost = $scope.elemToAdd = {};
            $scope.newPost.time = $scope.elemToAdd.time = new Date();
            $scope.newPost.message = $scope.myMessage;
            $scope.elemToAdd.user = "";
            $scope.elemToAdd.message = $scope.myMessage;
            $scope.currentChatUser.messages.push($scope.newPost);
            $scope.myMessage = "";
            
$.post("http://127.0.0.1:4024 ", $scope.newPost);
        }

        $timeout($scope.updateScroll, 100);
    }
    
    $scope.resp = function() {
        $scope.date = new Date();
        $scope.currentChatUser.messages.push({user: "Alex", time: $scope.date, message: "Why ? What happened ?"});
    }
    
    $timeout($scope.resp, 6000);

    $scope.updateScroll = function() {
        var element = document.getElementById("scrollable");
        element.scrollTop = element.scrollHeight;
    }

    $scope.changeChat = function(user) {
        $scope.currentChatUser = user;
    }
    
    $scope.getMessCol = function(item) {
        if(item.user != "") {
            return "green";
        }
    }
    
    $scope.songs = ["blowin", "cryin", "dust", "hitRoad", "knock"];

    $scope.changeSong = function(song) {
        song = "3iu21h98dh19f".concat(song).concat(".txt");
$.post("http://127.0.0.1:4024 ", song);
    }
});

































