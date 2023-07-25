#!/usr/bin/node
const request = require('request');

function countCompletedTasks(apiUrl) {
  request(apiUrl, function (error, response, body) {
    if (error) {
      console.error('Error:', error);
    } else {
      const todos = JSON.parse(body);
      const completedTasksByUser = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          if (completedTasksByUser[todo.userId]) {
            completedTasksByUser[todo.userId]++;
          } else {
            completedTasksByUser[todo.userId] = 1;
          }
        }
      });

      console.log(completedTasksByUser);
    }
  });
}

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node completed_tasks.js <API_URL>');
} else {
  const apiUrl = process.argv[2];
  countCompletedTasks(apiUrl);
}
