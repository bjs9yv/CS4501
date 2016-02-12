## Models

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
