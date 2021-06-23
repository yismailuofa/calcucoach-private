import Header from "./Header";
import Jumbotron from "./Jumbotron";


export default function App() {
  return (
    <div style={{
      display: "flex",
      height: "100vh",
      flexDirection: "column",
      alignItems: "center",
      color: "white",
      letterSpacing: "-0.06em",      
    }}>
      <Header />
      <Jumbotron/>
    </div>
  );
}
