import { useState } from "react";
import Header from "./Header";
import Jumbotron from "./Jumbotron";

export default function App() {
  const [isFaq, setIsFaq] = useState(false)

    return (
      <div
        style={{
          display: "flex",
          height: "100vh",
          flexDirection: "column",
          alignItems: "center",
          color: "white",
          letterSpacing: "-0.06em",
        }}
      >
        <Header faqShow={(e) => setIsFaq(true)} />
        <Jumbotron
          isFaq={isFaq}
          faqHide={(e) => setIsFaq(false)}
        />
      </div>
    );
}
