Collected Knowledge and Wisdom on

# Spotify Web API  
---  

## Provides:  
This API provides access to Spotify’s music catalog and user data. It allows for the creation of web apps that can interact with Spotify's service which includes providing metadata of various content, and music playlists.

### Pain factor: 3  
(0=ezpz...5=nightmare)  

### Key Provisioning:  
- Register a developer account at the https://developer.spotify.com/dashboard.  
- Create an app to obtain a **Client ID** and **Client Secret**.  
- Implement OAuth 2.0 for user authorization to access specific scopes.  

### Quotas:  
- Spotify API checks for how many calls were made in a 30 second window. I cannot find specific rate limits. It is possible to apply for a higher quota. 

---  

## The Good:  
- Well-documented with examples + charts + tutorials
- Explains various concepts that may be new to a new user
- Provides a sample/tutorial of how to set it up (JS only)

## The Bad:  
- Requires OAuth setup 
- Way too many refs 

## The Ugly:  
- No offline access—requires internet connectivity for every API call.  
- Token expiration can lead to user disruption if refresh flows aren’t properly handled.  

**Location:** [Spotify Web API Documentation](https://developer.spotify.com/documentation/web-api/)  

---  

Accurate as of (last update): 2024-11-25 

Contributors:  
the two spaces after each name are important!  
Tiffany Yang p5  
