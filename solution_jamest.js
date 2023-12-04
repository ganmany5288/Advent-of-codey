
// File input
const fs = require('fs')
const path = require('path')


// Total
var sum_possible = 0

// Conditions
var red = 12
var green = 13
var blue = 14

// var condition = false


// Function to read file and process each line
function processFile(filePath,sum_possible) {
    fs.readFile(filePath, 'utf8', function(err, data) {
        if (err) {
            console.error('Error reading the file:', err);
            return;
        }

        // Splitting the file content into lines
        // Whatever the fuck this means
        const lines = data.split(/\r?\n/);
        var failed = false;
        // console.log(lines);
        // Looping through each line
        lines.forEach((line, index) => {
            // console.log(line);
            var games = line.split(":")
            var game = games[0]
            var sets = games[1].split(";")
            // console.log(game)
            console.log(sets)
            // console.log(sets[0])

            for (let i = 0; i < sets.length; i++){
                var set = sets[i]
                var set_test = set.split(',')
                // console.log(set)
                // console.log(set_test)
                for (let j = 0; j < set_test.length; j++){
                    var color = set_test[j].trimStart().split(" ")
                    // console.log(color)
                    if (color[1] == "red"){
                        // Failed
                        if (color[0] > red){
                            // console.log(game.split(" ")[1])
                            // sum_possible += parseInt(game.split(" ")[1]) // this is so bad omfg
                            failed = true
                        }
                    }
                    if (color[1] == "blue"){
                        // Failed
                        if (color[0] > blue){
                            // sum_possible += parseInt(game.split(" ")[1]) // this is so bad omfg
                            failed = true
                        }
                    }
                    if (color[1] == "green"){
                        // Failed
                        if (color[0] > green){
                            // sum_possible += parseInt(game.split(" ")[1]) // this is so bad omfg
                            failed = true
                        }
                    }
                    // console.log(sum_possible)
                }
                // console.log(sets[i])
            }
            // console.log(failed)
            // console.log("=====================================")
            if (failed == false){
                sum_possible += parseInt(game.split(" ")[1])

            }else if (failed == true){
                failed = false
            }
            // console.log(`Line ${index + 1}: ${line}`);
            // Process each line as needed
        });
        console.log(sum_possible)
    });
    // console.log(sum_possible)
}

// Replace 'yourfile.txt' with the path to your file
const filePath = path.join(__dirname, 'input.txt');
processFile(filePath,sum_possible);



