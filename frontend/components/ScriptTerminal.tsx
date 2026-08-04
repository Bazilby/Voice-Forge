import { useEffect, useState } from "react";

type SystemStatus = {
    system: string;
    checks: {
        name: string;
        status: string;
    }[];
};

type ScriptTerminalProps = {
    status: SystemStatus | null;
};

function ScriptTerminal({ status }: ScriptTerminalProps) {
    const[bootText, setBootText] = useState("");
    const[booting, setBooting] = useState(true);

    const bootMessage = status
    ? `${status.system}

    SYSTEM CHECK...

    ${status.checks
        .map(check =>
            `${check.name.padEnd(20, ".")} ${check.status}`
        )
        .join("\n")}

    READY`
        : `BLACK LOOM VOICE FORGE MK.1

    CONNECTING TO SYSTEM...`;

            console.log("STATUS RECEIVED: ", status);
        

    useEffect(() => {

        setBootText("");
        setBooting(true);

        let current = 0;
        let timer: number;

        function typeCharacter() {

            if (current >= bootMessage.length) {

                timer = window.setTimeout(() => {
                    setBooting(false);
                }, 1200);

                return;
            }

            setBootText(
                bootMessage.slice(0, current + 1)
            );

            current++;

            const char = bootMessage[current];

            let delay = 35;

            if (char === "\n") delay = 220; 
            else if (char === ".") delay = 80;
            else  if (char === " ") delay = 20;

            timer = window.setTimeout(typeCharacter, delay);

        }

        typeCharacter();

        return () => {
            window.clearTimeout(timer);
        }

    }, [bootMessage]);

    return(

        <div
            className="
                h-full
                bg-[#171914]
                border
                border-zinc-700
                rounded-xl
                p-3

                shadow-inner
                crt-text
            "
        >
            <div  className="crt-screen">
                {booting && (
                    <div
                        className="
                            absolute
                            inset-0
                            z-10

                            bg-[#050704]

                            p-6

                            text-amber-200
                            font-mono
                            text-sm

                            whitespace-pre-line

                            crt-text
                        "
                    >
                        {bootText}
                        <span className="crt-cursor">_</span>
                    </div>
                )}
                <textarea
                    className="
                        w-full
                        h-96
                        resize-none
                        overflow-y-auto

                        bg-[#050704]

                        text-amber-200
                        font-mono
                        text-sm

                        p-6

                        rounded-lg

                        border
                        border-zinc-800

                        outline-none

                        focus:border-amber-900
                        shadow-inner
                        crt-text
                        crt-scroll
                    "
                    placeholder="Enter text..."
                />
            </div>
        </div>
        
    );  
}

export default ScriptTerminal;