function sortList() {
    var list, i, switching, b, shouldSwitch;

    list = document.getElementById("all-memebers");

    switching = true;
    /* Make a loop that will continue until
    no switching has been done: */

    while (switching) {

      switching = false;
      b = list.getElementsByTagName("LI");

      for (i = 0; i < (b.length - 1); i++) {
        shouldSwitch = false;
        
        /* Check if the next item should
        switch place with the current item: */
        if (b[i].innerHTML.toLowerCase() > b[i + 1].innerHTML.toLowerCase()) {
          /* If next item is alphabetically lower than current item,
          mark as a switch and break the loop: */
          shouldSwitch = true;
          break;
        }
      }
      if (shouldSwitch) {
        /* If a switch has been marked, make the switch
        and mark the switch as done: */
        b[i].parentNode.insertBefore(b[i + 1], b[i]);
        switching = true;
      }
    }
  }