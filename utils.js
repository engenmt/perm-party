let hello = 'world'
function mySubmitFunction(e) {
    e.preventDefault()
    enumerate()
    return false
}

function enumerate() {
    const basis = document.getElementById('basis').value
    const maxLength = document.getElementById('max-length').value
    const enumerateByBasis = pyscript.interpreter.globals.get('enumerate_by_basis')
    enumerateByBasis(basis, maxLength)
}

// function logRandom() {
//     const enumeration = pyscript.interpreter.globals.get('get_random')
//     enumeration()
// }

let pyScriptReady = false
function onPyScriptReady() {
    pyScriptReady = true
}