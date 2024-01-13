let new_exercise_test_payload = {

    "exercise":{
        "first": 1,
        "second": 6
    }
}

function new_exercise(){
    let exercise_string = new_exercise_test_payload.exercise.first + " X " + new_exercise_test_payload.exercise.second

    document.getElementById("ExerciseText").innerHTML = exercise_string
}