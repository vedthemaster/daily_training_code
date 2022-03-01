describe('Login Form Tests', () => {

	context('Testing the Login Form', () => {

			// TEST #1 -------------------------------------------------------------------------

			it('with Valid Credentials', () => {

				let userId = 'vedpatel3392@mail.com';
				let password = 'Master@911';

				// Navigate to Home page, after opening the browser
				cy.visit('https://localhost:44320/');

				// Enforce step-by-step execution of Cypress
				cy.pause();

				// Check if the Home Page Title is correct.
				cy.title().should('eq', 'Home page - University_Management');

				// Check if the hyperlink element to authenticate user contains the text "Login"
				// and after asserting that, click the link.
				cy.get('a[href="/Identity/Account/Login"]').contains('Login').click();

				// Now check if the Login Page appears
				cy.title().should('eq', 'Log in - University_Management');

				// Next enter valid login credentials into the two textboxes
				cy.get('input[id="Input_Email"]').type(userId);
				// cy.get('input[id="Input_Password"]').type(password);

				cy.pause();

				// Click on the Login button
				cy.get('button[type="submit"]').click();

				// Now check if the UserName is reflected on the home page, to confirm successful login.
				cy.get('div[class="text-danger validation-summary-valid"]').contains("The Password field is required.");

		

			});

	});

});