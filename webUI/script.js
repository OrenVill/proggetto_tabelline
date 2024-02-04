let new_exercise_test_payload = {

    "exercise":{
        "numbers":[2, 4, 2],
        "operations":["X", ":"]
    }
}

function new_exercise(){
    // let exercise_string = new_exercise_test_payload.exercise.first.toString() + new_exercise_test_payload.exercise.operation + new_exercise_test_payload.exercise.second.toString()
    let exercise_string = ""
    let i = 0
    let result = new_exercise_test_payload.exercise.numbers[0]

    while (i < new_exercise_test_payload.exercise.numbers.length){
        exercise_string += new_exercise_test_payload.exercise.numbers[i].toString()
        if (i < new_exercise_test_payload.exercise.operations.length) {
            exercise_string +=  " " + new_exercise_test_payload.exercise.operations[i] + " "
        }

        if (i > 0){
            switch(new_exercise_test_payload.exercise.operations[i-1]){
                case "X":
                    result *= new_exercise_test_payload.exercise.numbers[i]
                    break
                case ":":
                    result /= new_exercise_test_payload.exercise.numbers[i]
                    break
                // case "+":
                //     result += new_exercise_test_payload.exercise.numbers[i]
                //     console.log(result, "+")
                //     break
                // case "-":
                //     result -= new_exercise_test_payload.exercise.numbers[i]
                //     console.log(result, "-")
                //     break
            }
        }
        
        i++
    }        

    document.getElementById("ExerciseText").innerHTML = exercise_string

    console.log(result)

}
