function reverseCapitalize(word) {
    
    var backward = word.split("").reverse().join("");
    var capitalLetter = backward.toUpperCase();
    console.log(capitalLetter)

}
reverseCapitalize('father')