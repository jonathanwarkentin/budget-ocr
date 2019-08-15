# budget-ocr
A budgeting app based on receipt scanning.

## Minimum Viable Product (MVP)
### Part 1: Optical Character Recognition (OCR)
* Get basic OCR working (with pytesseract?)
* Make OCR work for receipt scans
* Make OCR work for cell phone photos of receipts

### Part 2: Flask API
* Hello World Flask App
* File Upload
* Call OCR module on API call with picture attached
* Return string output

### Part 3: Spreadsheet Business Logic
* Parse OCR output into spreadsheet/DB
* Sort into helpful categories

### Part 4: Mobile UI
* Make PWA / native / cross-platform app that takes picture of receipt with ideal camera settings, sends to API, displays resulting spreadsheet
---

## Possible Future Features
### Users
* Login
* DB for each user for ongoing analysis (IMPORTANT - allows for input of multiple receipts, so analysis can have multiple data points). PostgreSQL? Or use Google Sheets w/ API as DB (if already using Google Sheets for output)

### Direct Spreadsheet Editing
* Allow users to add/delete items in DB and edit pre-existing items (IMPORTANT for when OCR inevitably reads things wrong)

### Customization
* Users can perform custom analysis on their input (Different categories, etc.)

### Heavier UI
* Present results in distinct, native (looking) mobile app / PWA ( as opposed to just showing a spreadsheet)

