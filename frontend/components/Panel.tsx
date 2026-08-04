type PanelProps = {
    title: string;
    children: React.ReactNode;
    className?: string;
    status?:  "booting" | "ready" | "fault";
};

function Panel({ 
    title, 
    children, 
    className,
    status = "ready"
}: PanelProps) {
    return (
        <section
            className={`
              relative
              rounded-xl
              border
              border-[#45483a]
              bg-[#25291f]
              shadow-2xl
              overflow-hidden
              ${className  ?? ""}
            `}
        >
            {/* corner screws */}
            <div className="absolute top-2  left-2 w-3  h-3 rounded-full 
            bg-gradient-br from-zinc-500 to-zinc-700 border border-zinc-700 shadow-inner">
              <div
                    className="
                        absolute
                        top-1/2
                        left-1/2

                        w-2
                        h-[1px]

                        -translate-x-1/2
                        -translate-y-1/2

                        bg-zinc-800
                    "
                />  
            </div>
            <div className="absolute top-2 right-2 w-3 h-3 rounded-full 
            bg-gradient-br from-zinc-500 to-zinc-700 border border-zinc-700 shadow-inner">
                <div
                    className="
                        absolute
                        top-1/2
                        left-1/2

                        w-2
                        h-[1px]

                        -translate-x-1/2
                        -translate-y-1/2

                        bg-zinc-800
                    "
                />  
            </div>
            <div className="absolute bottom-2 left-2 w-3 h-3 rounded-full 
            bg-gradient-br from-zinc-500 to-zinc-700 border border-zinc-700 shadow-inner">
                <div
                    className="
                        absolute
                        top-1/2
                        left-1/2

                        w-2
                        h-[1px]

                        -translate-x-1/2
                        -translate-y-1/2

                        bg-zinc-800
                    "
                />  
            </div>
            <div className="absolute bottom-2 right-2 w-3 h-3 rounded-full 
            bg-gradient-br from-zinc-500 to-zinc-700 border border-zinc-700 shadow-inner">
                <div
                    className="
                        absolute
                        top-1/2
                        left-1/2

                        w-2
                        h-[1px]

                        -translate-x-1/2
                        -translate-y-1/2

                        bg-zinc-800
                    "
                />  
            </div>

            {/* Header */}
            <div
                className="
                    flex
                    items-center
                    justify-between
                    px-8
                    py-4
                    border-b
                    border-zinc-700
                    bg-[#20221d]    
                    shadow-[inset_0_-2px_3px_rgba(0,0,0,.35)]
                "
            >
                <div
                    className="
                        px-4
                        py-1

                        rounded

                        border
                        border-[#575c4d]

                        bg-[#2d3028]

                        shadow-inner
                    "
                >
                    <h2
                        className="
                            uppercase
                            tracking-[0.3em]
                            text-sm
                            font-bold
                            text-zinc-300
                            drop-shadow-md
                        "
                    >
                        {title}
                    </h2>
                </div>

                <div className="flex items-center gap-5">

                    <div className="flex items-center gap-2">

                        <div
                            className={`
                                w-2
                                h-2
                                rounded-full
                                border
                                border-zinc-700

                                ${
                                    status === "ready"
                                        ? "bg-amber-300 shadow-[0_0_10px_rgba(252,211,77,.9)]"
                                        : "bg-[#353535]"
                                }
                            `}
                        />

                        <span
                            className={`
                                text-xs
                                tracking-widest

                                ${
                                    status === "ready"
                                        ? "text-amber-200"
                                        : "text-zinc-700"
                                }
                            `}
                        >
                            READY
                        </span>

                    </div>

                    <div className="flex items-center gap-2">

                        <div
                            className={`
                                w-2
                                h-2
                                rounded-full
                                border
                                border-zinc-700

                                ${
                                    status === "fault"
                                        ? "bg-red-500 animate-pulse shadow-[0_0_10px_rgba(239,68,68,.8)]"
                                        : "bg-[#353535]"
                                }
                            `}
                        />

                        <span
                            className={`
                                text-xs
                                tracking-widest

                                ${
                                    status === "fault"
                                        ? "text-red-400"
                                        : "text-zinc-700"
                                }
                            `}
                        >
                            FAULT
                        </span>

                    </div>

                </div>

            </div>
        
            {/* Content */}
            <div  
                className="
                    m-3
                    p-5
                    rounded-lg
                    border
                    border-zinc-800
                    bg-[#11130f]
                    shadow-inner
                "
            >
                {children}
            </div>
        </section>
    );
}

export default Panel;