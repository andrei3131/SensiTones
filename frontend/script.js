var chatApp = angular.module('chatApp', []);

chatApp.controller('mainController', function($scope) {
    $scope.messages = [{time: "2017-02-04T19:10:21.932Z", message: "Hi, how are you?"},
    {time: "2017-02-04T19:12:21.932Z", message: "Good, you?"},
    {time: "2017-02-04T19:14:21.932Z", message: "Good"}];

    
    $scope.post_mess = function() {
        
        $scope.newPost = {};
        $scope.newPost.time = new Date();
        $scope.newPost.message = $scope.myMessage;
        
        console.log($scope.newPost);
        
        $scope.messages.push($scope.newPost);
        $scope.myMessage = "";
        //$.post("http://127.0.0.1:3600", x);
    }
});
