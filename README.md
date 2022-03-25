# ScriveAssignment

This repo tests the following things:

    * Go to https://staging.scrive.com/t/9221714692410699950/7348c782641060a9
    * Fill in the full name in the document.
    * Click on Next
    * There should be a confirmation modal (the one that has text "by clicking the button you will..."). Take a screenshot of this confirmation modal and try to make it only show what is actually visible in the modal (not the whole web page).
    * Sign the document
    * Verify that there is a text “Document signed” on the screen.
   
The tests runs through following steps:
1. Tests on Chrome
2. Tests on Firefox
3. Tests on ie11 via browserstack.

After each step, Screen shots are saved under /screenshots folder.
