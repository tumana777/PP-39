const button = document.getElementById('button');
const course = document.getElementById('course');
const student = document.getElementById('student');

let changed = false;

button.addEventListener('click', function() {
    changed = !changed;

    course.innerText = changed ? 'JavaScript' : 'Python';
    student.innerText = changed ? 'Davit' : 'Otar';

    console.log('Button clicked, changed:', changed);
});
