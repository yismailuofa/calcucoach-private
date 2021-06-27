import FaqBack from "./FaqBack";
import FaqText from "./FaqText";
import { CSSTransition } from "react-transition-group";
import "./styles/slideY.css"

export default function FaqScreen({ faqHide, isFaq }) {
  return (
    <CSSTransition in={isFaq} timeout={1400} classNames="slideY" unmountOnExit={true} >
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          position: "absolute",
        }}
      >
        <FaqText />
        <FaqBack faqHide={faqHide} />
      </div>
    </CSSTransition>
  );
}
