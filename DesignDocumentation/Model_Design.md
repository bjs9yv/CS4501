# Models

### User 
- Username (10 character alpha-numeric string)
- Public key (string)
- Bitcoin credit (float)
- Bitcoin address (string)
- One or more Bitcoin accounts (string)
- Rating (integer)
- Purchases (List of Listings)
- Direct Messages(List of strings)
- Seller (boolean)
- Products (List of Listings)

### Listing 
- Title (string)
- Description (string)
- Bitcoin cost (string)
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
