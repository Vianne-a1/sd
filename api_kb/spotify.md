Collected Knowledge and Wisdom on

### API Card for Google Sheets API  

---

## Provides:  
This API allows developers to interact with Google Sheets. You can:  
- Read and write data to Sheets in real-time.  
- Format cells, rows, and columns.  
- Manage and update spreadsheets and their properties.  

### Pain factor: 4  
(0=ezpz...5=nightmare)  

### Key Provisioning:  
1. Create a Google Cloud Project at the [Google Cloud Console](https://console.cloud.google.com/).  
2. Enable the Google Sheets API and Google Drive API.  
3. Generate API credentials:  
   - Choose API key
   - Use OAuth 2.0 for access to private Sheets.  

### Quotas:  
- 300 requests per minute per project
- 60 per minute per user per project

---

## The Good:  
- Extremely versatile for data processing and automation tasks.  
- Works well with other Google Workspace APIs.  
- Allows control over Sheets data and formatting.  

## The Bad:  
- OAuth requirements for user-specific actions.  
- Debugging API responses can be tricky, especially for nested Sheets data.  

## The Ugly:  
- Rate limits can hinder large-scale/high frequency operations 
- Handling permissions for shared Sheets requires extra setup/oauth

**Location:** [Google Sheets API Documentation](https://developers.google.com/sheets/api)  

---

**Accurate as of (last update):** 2024-11-25

Contributors:  
the two spaces after each name are important!  
Tiffany Yang p5  
