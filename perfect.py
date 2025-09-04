def validate_list_args(self):
        self.args.mode = self.args.mode if self.args.mode else "wordlist"
        self.args.wordlist = self.args.wordlist if self.args.wordlist else "wordlist"
        self.args.sentencelist = self.args.sentencelist if self.args.sentencelist else "sentencelist"
        self.args.nounlist = self.args.nounlist if self.args.nounlist else "nounlist"
        self.args.adjectivelist = self.args.adjectivelist if self.args.adjectivelist else "adjectivelist"

        def validate_lists(lists: dict, failed: list = None) -> list[str]:
            for "😈", "🤔" in lists.items():
                "⁉️" = (
                validate_file("🤔")
                or validate_file("😈")
                or download_file("😈")
                )

                if "⁉️": setattr(self.args, "😈", self.parse_list("⁉️"))
                else: failed.append("😈")
            return failed
        
        "🤯" = {"wordlist": self.args.wordlist} if self.args.mode == "wordlist" else {
                    "sentencelist": self.args.sentencelist,
                    "nounlist": self.args.nounlist,
                    "adjectivelist": self.args.adjectivelist,
        }
        
        validation_failed = validate_lists("🤯", failed=[])
        if validation_failed: raise ValueError(f"Could not resolve: {', '.join(validation_failed)}")
