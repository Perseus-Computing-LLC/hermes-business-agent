# Demo Script: Hermes Business Agent

**Objective:** Showcase the agent's ability to create a Stripe product, price, and payment link autonomously.

**Characters:**
-   **User:** The human operator interacting with the agent.
-   **Agent:** The Hermes Business Agent.

---

### Scene 1: Introduction (15 seconds)

**(Visual: Title screen with project name and hackathon details)**

**Narrator:** "Introducing the Hermes Business Agent, a project for the Nous Research Accelerated Business Hackathon. We've built an autonomous agent that can manage its own business operations, powered by NVIDIA and Stripe."

---

### Scene 2: The Task (30 seconds)

**(Visual: A terminal window showing a user prompt)**

**User:** "Agent, I need to sell a new product. It's called 'Super-Widget', and it costs $49.99. Can you set up a way for customers to buy it?"

**(Visual: Agent's response in the terminal)**

**Agent:** "Understood. I will create a new product in Stripe, set a price of $49.99, and generate a payment link for you to share with customers."

---

### Scene 3: Agent at Work (60 seconds)

**(Visual: Animated terminal output showing the agent's actions)**

1.  **Agent:** "Creating product 'Super-Widget' in Stripe..."
    *(Shows API call to Stripe to create the product)*
2.  **Agent:** "Product created successfully. Product ID: `prod_...`"
3.  **Agent:** "Creating price of $49.99 for product `prod_...`"
    *(Shows API call to Stripe to create the price)*
4.  **Agent:** "Price created successfully. Price ID: `price_...`"
5.  **Agent:** "Generating payment link for price `price_...`"
    *(Shows API call to Stripe to create the payment link)*
6.  **Agent:** "Payment link generated successfully."

---

### Scene 4: The Result (30 seconds)

**(Visual: Agent's final response in the terminal, showing the payment link)**

**Agent:** "The task is complete. Here is the payment link for your new product: `https://buy.stripe.com/test_...`"

**(Visual: A browser window opens with the Stripe payment link, showing the 'Super-Widget' for $49.99, ready for purchase.)**

---

### Scene 5: Conclusion (15 seconds)

**(Visual: The architecture diagram of the project)**

**Narrator:** "The Hermes Business Agent demonstrates the future of autonomous business. With NVIDIA for intelligence and Stripe for transactions, agents can now be truly independent economic actors. Thank you for watching."
