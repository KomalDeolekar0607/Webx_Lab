// app.js

// 🔸 Define module
var app = angular.module('myApp', []);

// 🔸 Define controller
app.controller('MainController', function($scope, AuthService) {
    $scope.username = '';
    $scope.password = '';
    $scope.loginMessage = '';

    // 📌 Login Function
    $scope.login = function() {
        if (AuthService.authenticate($scope.username, $scope.password)) {
            $scope.loginMessage = "Login successful!";
        } else {
            $scope.loginMessage = "Invalid credentials!";
        }
    };

    // 📚 Book Data
    $scope.books = [
        { title: 'Harry Potter', author: 'J.K. Rowling', genre: 'Fantasy' },
        { title: 'The Hobbit', author: 'J.R.R. Tolkien', genre: 'Adventure' },
        { title: 'Clean Code', author: 'Robert C. Martin', genre: 'Programming' },
        { title: 'Atomic Habits', author: 'James Clear', genre: 'Self-help' }
    ];

    $scope.searchText = '';
});

// 🔸 Create Custom Service for Authentication
app.service('AuthService', function() {
    var validUsername = "admin";
    var validPassword = "1234";

    this.authenticate = function(username, password) {
        return username === validUsername && password === validPassword;
    };
});

// 🔸 Custom Filter for Book Search
app.filter('bookFilter', function() {
    return function(books, searchText) {
        if (!searchText) return books;
        searchText = searchText.toLowerCase();

        return books.filter(function(book) {
            return book.title.toLowerCase().includes(searchText) ||
                   book.author.toLowerCase().includes(searchText) ||
                   book.genre.toLowerCase().includes(searchText);
        });
    };
});
