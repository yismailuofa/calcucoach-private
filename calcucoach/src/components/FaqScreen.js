import FaqBack from "./FaqBack";
import FaqText from "./FaqText";
import { CSSTransition } from "react-transition-group";
import "./styles/slideY.css";
import { useRef } from "react";

export default function FaqScreen({ faqHide, isFaq }) {
  const nodeRef = useRef(null);
  return (
    <CSSTransition
      in={isFaq}
      timeout={1400}
      classNames="slideY"
      unmountOnExit={true}
      nodeRef={nodeRef}
    >
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          position: "absolute",
        }}
        ref={nodeRef}
      >
        <FaqText />
        <FaqBack faqHide={faqHide} />
      </div>
    </CSSTransition>
  );
}
