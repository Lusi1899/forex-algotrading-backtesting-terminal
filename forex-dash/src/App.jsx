import NavigationBar from "./components/NavigationBar.jsx";
import Home from "./pages/Home.jsx";
import Footer from "./components/Footer.jsx";
import Dashboard from "./pages/Dashboard.jsx";
import {
BrowserRouter,
Route,
Routes
} from 'react-router-dom';

function App() {
  return (
  <>
  <BrowserRouter>
    <div id="app-holder" >
    <NavigationBar />
       <div className="container">
            <Routes>
                 <Route exact path="/" element={<Home />}/>
                 <Route exact path="/dashboard" element={<Dashboard />}/>

             </Routes>

       </div>
<Footer/>
    </div>
    </BrowserRouter>
    </>
  );
}




export default App;
