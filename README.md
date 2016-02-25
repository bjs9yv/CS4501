# Overview

- Four Tier Django web application for CS 4501 Internet Scale Applications
  - Layer 1: MySQL database
  - Layer 2: Models API
  - Layer 3: Service level API
  - Layer 4: Web Interface

# Models

### User 
- Username (10 character alpha-numeric string)
- Public key (string)
- Bitcoin credit (float)
- One or more Bitcoin accounts (string)
- Rating (integer)
- Purchases (List of Listings)
- Seller (boolean)
- Products (List of Listings)

### Message
- sender
- recipient
- body
- opened

### Listing 
- Title (string)
- Description (string)
- Bitcoin cost (float)
- Merchant (User)
- Quantity Available (integer)

### Transaction
- Product
- Quantity
- Buyer
- Seller
- Status

### Escrow
- 

### Shopping Cart
- Products (List of Listings)

# User Stories

### Models Related

#### Users 
- As a User, when I make my account I want to upload my public key to my profile.
- As a User, when I make my account I want to optionally add Bitcoin addresses to use for withdraws.
- As a User, I want to credit my account with Bitcoins I send from a Bitcoin address.
- As a User, I want to direct message other Users.
- As a Seller, I want to know if the buyer is trustworthy.
- As a Buyer, I want to add products to a shopping cart.

#### Listings
- As a Seller, I want to post a new Listing.
- As a Seller, I want to specify available quantities for a new Listing.
- As a Buyer, I want to select the quantity I want if there are multiple quantites available.

#### Escrow Stuff
- As a Site Manager, I want a non finalized purchase to go into an escrow account I control. 

### Security Related
