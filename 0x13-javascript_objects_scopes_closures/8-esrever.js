#!/usr/bin/python3
exports.esrever = function (list) {
	const reverse = [];
	for (let i = list.length -1; i >= 0; i--) {
	  reverse.push(list[i]);
	}
	return reverse;
};
