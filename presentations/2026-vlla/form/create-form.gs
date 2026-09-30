/**
 * Creates the "Get the Zest code" Google Form for the VLLA 2026 talk.
 *
 * How to run:
 *   1. Go to https://script.google.com and click New project.
 *   2. Replace everything in Code.gs with this file and click Save.
 *   3. Choose createZestForm in the function menu and click Run.
 *      Approve the permissions prompt (it asks to manage your forms and sheets).
 *   4. Open View > Logs (or the Execution log). It prints the form's
 *      public link, a short link, the edit link and the response sheet.
 */
function createZestForm() {
  var form = FormApp.create('Get the Zest Code');

  form.setDescription(
    'Zest turns web interactives into graded Canvas assignments. ' +
    'Leave your details and we will email you when the code is released. ' +
    'We only use this to contact you about Zest.'
  );

  // Anyone can answer, including people outside Virtual Arkansas.
  try {
    form.setRequireLogin(false);
  } catch (e) {
    // Only applies to Google Workspace accounts; ignore elsewhere.
  }
  form.setCollectEmail(false);
  form.setLimitOneResponsePerUser(false);
  form.setAllowResponseEdits(false);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage(
    'Thanks! We will email you when the Zest code is released.'
  );

  form.addTextItem()
    .setTitle('Name')
    .setRequired(true);

  var emailCheck = FormApp.createTextValidation()
    .setHelpText('Please enter a valid email address.')
    .requireTextIsEmail()
    .build();
  form.addTextItem()
    .setTitle('Email address')
    .setValidation(emailCheck)
    .setRequired(true);

  form.addTextItem()
    .setTitle('Organization')
    .setHelpText('School, district, state program or company')
    .setRequired(true);

  var use = form.addMultipleChoiceItem();
  use.setTitle('How do you plan to use Zest?')
    .setChoices([
      use.createChoice('Run it for my school, district or program'),
      use.createChoice('Build interactive activities (zests) for our courses'),
      use.createChoice('Evaluate it for my organization'),
      use.createChoice('Share or trade zests with other programs'),
      use.createChoice('Just curious')
    ])
    .showOtherOption(true)
    .setRequired(true);

  // Responses also go to a spreadsheet in your Drive.
  var sheet = SpreadsheetApp.create('Get the Zest Code (Responses)');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, sheet.getId());

  var url = form.getPublishedUrl();
  var shortUrl = url;
  try {
    shortUrl = form.shortenFormUrl(url);
  } catch (e) {
    // Short links are not always available; the full link works too.
  }

  Logger.log('Public link (for the QR code): ' + url);
  Logger.log('Short link: ' + shortUrl);
  Logger.log('Edit link: ' + form.getEditUrl());
  Logger.log('Responses sheet: ' + sheet.getUrl());
}
