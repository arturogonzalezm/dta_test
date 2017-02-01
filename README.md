## Description

Login system that provides authentication to businesses.

## Specs

- Users can log in using this application system, but also using their Facebook and Google accounts.

- The businesses that the users are logging in to must not be able to share information about
users, so the task is to write some code that generates unique user IDs for different
businesses. 

- Each time the same user logs in to a specific business, that business should
receive a consistent user ID, but not the user's original login name. Each different business a
user logs in to must receive a different ID.

        Example:
        
        If Google user with login name "jess1234" logs in to Initech, Initech might be given
        the user ID "0009". When jess1234 logs in to Initrode, they might get "000A". Initech and
        Initrode receive different IDs for the same user, and therefore cannot share information about
        them.
        
        The ID should also be different for each login source, so jess1234 from Facebook should have a
        different generated ID from jess1234 from Google. There should be no collisions among
        generated IDs. IDs should only be ASCII case-sensitive alphanumeric strings or numbers.
        In addition, if the user is not logging into a white-listed business or from a white-listed source,
        then "error" should be printed.

## Rules

- Allowed businesses: initech, initrode
- Allowed login sources: facebook, google, local
- You will receive login information from stdin in the comma-separated format: Login_source,business,login_name
- A blank line ends the input.

        Example:
                
        facebook,initech,jess1234
        facebook,initrode,jess1234
        google,initech,jess1234
        google,initrode,jess1234
        local,initech,joe8844
        invalid,invalid,jax1313
        Facebook,initrode,jess1234

- The output should be the the same information, along with an extra field that is the generated ID: `login_source,business,login_name,user_id`
OR
`error`

        Example:
        
        facebook,initech,jess1234,0009
        facebook,initrode,jess1234,000a
        google,initech,jess1234,000b
        google,initrode,jess1234,000c
        local,initech,joe8844,000d
        error
        facebook,initrode,jess1234,000a

## Requirements

- Python 3.x
- MySQL
- Tested in CentOS 7.x OS and Mac OS X/OS X/macOS.

## Getting Started


