Installation

In the project directory, you can run:
npm install
npm start

Runs the app in the development mode.
Open http://localhost:3000 to view it in the browser.

The page will reload if you make edits.
You will also see any lint errors in the console.
View the Backend API Documentation
Watch the Demo Video Here
Inspiration

Going through the CNCF landscape and getting started with contributions gets overwhelming. We wanted to simplify the existing landscape for beginners and added a roadmap too for folks who want to learn more in the field of DevOps.

This platform is developed such that it can guide new folks and learn concepts such as Docker and Kubernetes even if they contribute to this project because of the tools used in this project such as Docker, Datree, Alan AI, Firebase, getstream.io and Twilio.
⚙ What it does -

    Simplified CNCF LandScape where you can filter, search projects to contribute according to your tech stack
    Get your questions answered about DevOps by Alan AI
    Get your own personalised roadmap to reach your goal of DevOps
    Twilio will alert the project admins if there occurs any error in the server and server is about to shut down
    Get your brains working and join, network with other contributors of CNCF in the chat channel powered by getstream.io

🔧 How we built it-

    Developed an API to get all the projects in the database and specific project from large project data. The project id is given by the database. This API will also give you number of project provided in limit field and you can increment the page no to get the next limit frame data along all names of the projects. Check out the documentation of API here
    The fronted/client consumes this api in order to fetch the details of the several cncf projects and their information which can be needed by the beginner.
    We used Alan AI to develop a DevOps FAQ and roadmap section which could guide beginners on how to get started. Check out the Alan assistant implemented here
    For folks to get more involved and carry the conversations on the platform itself we used getstream.io to created a messaging channel where you could ask anything related to CNCF.
    Want to escape the chaos caused by server failure? Yes we can! by the use of Twilio. We used it to get notifications before a server goes down.
