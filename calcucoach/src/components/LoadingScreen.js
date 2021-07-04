import { useRef, useEffect } from "react";
import { CSSTransition } from "react-transition-group";
import "./styles/slideX.css";

export default function LoadingScreen({
  nextStep,
  step
}) {
  const nodeRef = useRef(null);

useEffect(() => {
    if (step === 4) {
        const time = setTimeout(() => nextStep(), 0);
        return () => {
            clearTimeout(time)
        }
    }
})

  return (
    <CSSTransition
      in={step === 4}
      timeout={900}
      classNames="slideXmiddle"
      unmountOnExit={true}
      mountOnEnter={true}
      nodeRef={nodeRef}
    >
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          position: "absolute",
        }}
        ref={nodeRef}
      >
        <div
          style={{
            fontSize: "4vh",
            display: "flex",
            padding: "2vh",  
            borderRadius: "4vh",
            flexDirection: "column",
            alignItems: "center",
            background: "linear-gradient(180deg, rgba(74,134,186,1) 50%, rgba(51,96,136,1) 100%)"
          }}
        >
            Loading...
        </div>
      </div>
    </CSSTransition>
  );
}
