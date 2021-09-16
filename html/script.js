function addOptions(printers) {
    console.log("Cuando pasa esto?")
    var select = document.getElementById("printers")
    for (printer of printers) {
        var opt = document.createElement('option');
        opt.value = printer;
        opt.innerHTML = printer;
        select.appendChild(opt);
        if (printer.toLowerCase() == document.printers_printer) {
            opt.selected = true
        }
    }

}

data = getDataFromRB({module_name:"Printer", command_name:"get_printers"})
.then(data => {
    console.log(data["printers"])
    data["printers"].unshift("Seleccionar por variable")
    data["printers"].unshift("---- Select an option ----")
    printers = data["printers"]
    addOptions(printers)
})

