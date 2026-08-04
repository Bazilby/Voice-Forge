import { useState } from "react";

type ToggleSwitchProps = {
    label:string
};

function ToggleSwitch({ label }: ToggleSwitchProps) {
    const [enabled, setEnabled] = useState(false);

    return  (
        <div className = "flex items-center  justify-between w-full py-3">
            <span className="uppercase tracking-wider text-sm text-stone-300">
                {label}
            </span>

            <button
                onClick={() => setEnabled(!enabled)}
                className="relative w-14 h-8 flex-shrink-0"
            >
                <div
                    className="
                        absolute
                        inset=0
                        rounded-md
                        border
                        border-stone-700
                        bg-stone-900
                        shadow-inner
                    "
                />

                <div
                    className={`
                        absolute
                        top-1
                        w-5
                        h-6
                        rounded-sm
                        border
                        border-zinc-600
                        bg-zinc-400
                        transition-all
                        duration-200
                        ${enabled ? "left-8 rotate-12" : "left-1 -rotate-12"}
                    `}
                />

                

            </button>

        </div>
    );
}

export default ToggleSwitch;