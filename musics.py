from buzzer_music import music
from machine import Pin
song = "0 E6 1 0 0.75;1 E6 1 0 0.75;3 E6 1 0 0.75;5 C6 1 0 0.75;6 E6 1 0 0.75;8 G6 1 0 0.75;16 C6 1 0 0.75;19 G5 1 0 0.75;22 E5 1 0 0.75;25 A5 1 0 0.75;27 B5 1 0 0.75;29 A#5 1 0 0.75;30 A5 1 0 0.75;32 G5 1 0 0.75;33 E6 1 0 0.75;35 G6 1 0 0.75;36 A6 1 0 0.75;38 F6 1 0 0.75;39 G6 1 0 0.75;41 E6 1 0 0.75;43 C6 1 0 0.75;44 D6 1 0 0.75;45 B5 1 0 0.75;48 C6 1 0 0.75;51 G5 1 0 0.75;54 E5 1 0 0.75;57 A5 1 0 0.75;59 B5 1 0 0.75;61 A#5 1 0 0.75;62 A5 1 0 0.75;64 G5 1 0 0.75;65 E6 1 0 0.75;67 G6 1 0 0.75;68 A6 1 0 0.75;70 F6 1 0 0.75;71 G6 1 0 0.75;73 E6 1 0 0.75;75 C6 1 0 0.75;76 D6 1 0 0.75;77 B5 1 0 0.75;82 G6 1 0 0.75;83 F#6 1 0 0.75;84 F6 1 0 0.75;85 D#6 1 0 0.75;87 E6 1 0 0.75;89 G#5 1 0 0.75;90 A5 1 0 0.75;91 C6 1 0 0.75;93 A5 1 0 0.75;94 C6 1 0 0.75;95 D6 1 0 0.75;98 G6 1 0 0.75;99 F#6 1 0 0.75;100 F6 1 0 0.75;101 D#6 1 0 0.75;103 E6 1 0 0.75;105 C7 1 0 0.75;107 C7 1 0 0.75;108 C7 1 0 0.75;114 G6 1 0 0.75;115 F#6 1 0 0.75;116 F6 1 0 0.75;117 D#6 1 0 0.75;119 E6 1 0 0.75;121 G#5 1 0 0.75;122 A5 1 0 0.75;123 C6 1 0 0.75;125 A5 1 0 0.75;126 C6 1 0 0.75;127 D6 1 0 0.75;130 D#6 1 0 0.75;133 D6 1 0 0.75;136 C6 1 0 0.75;146 G6 1 0 0.75;147 F#6 1 0 0.75;148 F6 1 0 0.75;149 D#6 1 0 0.75;151 E6 1 0 0.75;153 G#5 1 0 0.75;154 A5 1 0 0.75;155 C6 1 0 0.75;157 A5 1 0 0.75;158 C6 1 0 0.75;159 D6 1 0 0.75;162 G6 1 0 0.75;163 F#6 1 0 0.75;164 F6 1 0 0.75;165 D#6 1 0 0.75;167 E6 1 0 0.75;169 C7 1 0 0.75;171 C7 1 0 0.75;172 C7 1 0 0.75;178 G6 1 0 0.75;179 F#6 1 0 0.75;180 F6 1 0 0.75;181 D#6 1 0 0.75;183 E6 1 0 0.75;185 G#5 1 0 0.75;186 A5 1 0 0.75;187 C6 1 0 0.75;189 A5 1 0 0.75;190 C6 1 0 0.75;191 D6 1 0 0.75;194 D#6 1 0 0.75;197 D6 1 0 0.75;200 C6 1 0 0.75;208 C6 1 0 0.75;209 C6 1 0 0.75;211 C6 1 0 0.75;213 C6 1 0 0.75;214 D6 1 0 0.75;216 E6 1 0 0.75;217 C6 1 0 0.75;219 A5 1 0 0.75;220 G5 1 0 0.75;224 C6 1 0 0.75;225 C6 1 0 0.75;227 C6 1 0 0.75;229 C6 1 0 0.75;230 D6 1 0 0.75;231 E6 1 0 0.75;240 C6 1 0 0.75;241 C6 1 0 0.75;243 C6 1 0 0.75;245 C6 1 0 0.75;246 D6 1 0 0.75;248 E6 1 0 0.75;249 C6 1 0 0.75;251 A5 1 0 0.75;252 G5 1 0 0.75;256 E6 1 0 0.75;257 E6 1 0 0.75;259 E6 1 0 0.75;261 C6 1 0 0.75;262 E6 1 0 0.75;264 G6 1 0 0.75;272 C6 1 0 0.75;275 G5 1 0 0.75;278 E5 1 0 0.75;281 A5 1 0 0.75;283 B5 1 0 0.75;285 A#5 1 0 0.75;286 A5 1 0 0.75;288 G5 1 0 0.75;289 E6 1 0 0.75;291 G6 1 0 0.75;292 A6 1 0 0.75;294 F6 1 0 0.75;295 G6 1 0 0.75;297 E6 1 0 0.75;299 C6 1 0 0.75;300 D6 1 0 0.75;301 B5 1 0 0.75;304 C6 1 0 0.75;307 G5 1 0 0.75;310 E5 1 0 0.75;313 A5 1 0 0.75;315 B5 1 0 0.75;317 A#5 1 0 0.75;318 A5 1 0 0.75;320 G5 1 0 0.75;321 E6 1 0 0.75;323 G6 1 0 0.75;324 A6 1 0 0.75;326 F6 1 0 0.75;327 G6 1 0 0.75;329 E6 1 0 0.75;331 C6 1 0 0.75;332 D6 1 0 0.75;333 B5 1 0 0.75;336 E6 1 0 0.75;337 C6 1 0 0.75;339 G5 1 0 0.75;342 G#5 1 0 0.75;344 A5 1 0 0.75;345 F6 1 0 0.75;347 F6 1 0 0.75;348 A5 1 0 0.75;352 B5 1 0 0.75;353 A6 1 0 0.75;355 A6 1 0 0.75;356 A6 1 0 0.75;357 G6 1 0 0.75;359 F6 1 0 0.75;360 E6 1 0 0.75;361 C6 1 0 0.75;363 A5 1 0 0.75;364 G5 1 0 0.75;368 E6 1 0 0.75;369 C6 1 0 0.75;371 G5 1 0 0.75;374 G#5 1 0 0.75;376 A5 1 0 0.75;377 F6 1 0 0.75;379 F6 1 0 0.75;380 A5 1 0 0.75;0 F#5 1 0 0.75;1 F#5 1 0 0.75;3 F#5 1 0 0.75;5 F#5 1 0 0.75;6 F#5 1 0 0.75;8 B5 1 0 0.75;12 G5 1 0 0.75;16 E5 1 0 0.75;19 C5 1 0 0.75;22 G4 1 0 0.75;25 C5 1 0 0.75;27 D5 1 0 0.75;29 C#5 1 0 0.75;30 C5 1 0 0.75;32 C5 1 0 0.75;33 G5 1 0 0.75;35 B5 1 0 0.75;36 C6 1 0 0.75;38 A5 1 0 0.75;39 B5 1 0 0.75;41 A5 1 0 0.75;43 E5 1 0 0.75;44 F5 1 0 0.75;45 D5 1 0 0.75;48 E5 1 0 0.75;51 C5 1 0 0.75;54 G4 1 0 0.75;57 C5 1 0 0.75;59 D5 1 0 0.75;61 C#5 1 0 0.75;62 C5 1 0 0.75;64 C5 1 0 0.75;65 G5 1 0 0.75;67 B5 1 0 0.75;68 C6 1 0 0.75;70 A5 1 0 0.75;71 B5 1 0 0.75;73 A5 1 0 0.75;75 E5 1 0 0.75;76 F5 1 0 0.75;77 D5 1 0 0.75;82 E6 1 0 0.75;83 D#6 1 0 0.75;84 D6 1 0 0.75;85 B5 1 0 0.75;87 C6 1 0 0.75;89 E5 1 0 0.75;90 F5 1 0 0.75;91 G5 1 0 0.75;93 C5 1 0 0.75;94 E5 1 0 0.75;95 F5 1 0 0.75;98 E6 1 0 0.75;99 D#6 1 0 0.75;100 D6 1 0 0.75;101 B5 1 0 0.75;103 C6 1 0 0.75;105 F6 1 0 0.75;107 F6 1 0 0.75;108 F6 1 0 0.75;114 E6 1 0 0.75;115 D#6 1 0 0.75;116 D6 1 0 0.75;117 B5 1 0 0.75;119 C6 1 0 0.75;121 E5 1 0 0.75;122 F5 1 0 0.75;123 G5 1 0 0.75;125 C5 1 0 0.75;126 E5 1 0 0.75;127 F5 1 0 0.75;130 G#5 1 0 0.75;133 F5 1 0 0.75;136 E5 1 0 0.75;146 E6 1 0 0.75;147 D#6 1 0 0.75;148 D6 1 0 0.75;149 B5 1 0 0.75;151 C6 1 0 0.75;153 E5 1 0 0.75;154 F5 1 0 0.75;155 G5 1 0 0.75;157 C5 1 0 0.75;158 E5 1 0 0.75;159 F5 1 0 0.75;162 E6 1 0 0.75;163 D#6 1 0 0.75;164 D6 1 0 0.75;165 B5 1 0 0.75;167 C6 1 0 0.75;169 F6 1 0 0.75;171 F6 1 0 0.75;172 F6 1 0 0.75;178 E6 1 0 0.75;179 D#6 1 0 0.75;180 D6 1 0 0.75;181 B5 1 0 0.75;183 C6 1 0 0.75;185 E5 1 0 0.75;186 F5 1 0 0.75;187 G5 1 0 0.75;189 C5 1 0 0.75;190 E5 1 0 0.75;191 F5 1 0 0.75;194 G#5 1 0 0.75;197 F5 1 0 0.75;200 E5 1 0 0.75;208 G#5 1 0 0.75;209 G#5 1 0 0.75;211 G#5 1 0 0.75;213 G#5 1 0 0.75;214 A#5 1 0 0.75;216 G5 1 0 0.75;217 E5 1 0 0.75;219 E5 1 0 0.75;220 C5 1 0 0.75;224 G#5 1 0 0.75;225 G#5 1 0 0.75;227 G#5 1 0 0.75;229 G#5 1 0 0.75;230 A#5 1 0 0.75;231 G5 1 0 0.75;240 G#5 1 0 0.75;241 G#5 1 0 0.75;243 G#5 1 0 0.75;245 G#5 1 0 0.75;246 A#5 1 0 0.75;248 G5 1 0 0.75;249 E5 1 0 0.75;251 E5 1 0 0.75;252 C5 1 0 0.75;256 F#5 1 0 0.75;257 F#5 1 0 0.75;259 F#5 1 0 0.75;261 F#5 1 0 0.75;262 F#5 1 0 0.75;264 B5 1 0 0.75;268 G5 1 0 0.75;272 E5 1 0 0.75;275 C5 1 0 0.75;278 G4 1 0 0.75;281 C5 1 0 0.75;283 D5 1 0 0.75;285 C#5 1 0 0.75;286 C5 1 0 0.75;288 C5 1 0 0.75;289 G5 1 0 0.75;291 B5 1 0 0.75;292 C6 1 0 0.75;294 A5 1 0 0.75;295 B5 1 0 0.75;297 A5 1 0 0.75;299 E5 1 0 0.75;300 F5 1 0 0.75;301 D5 1 0 0.75;304 E5 1 0 0.75;307 C5 1 0 0.75;310 G4 1 0 0.75;313 C5 1 0 0.75;315 D5 1 0 0.75;317 C#5 1 0 0.75;318 C5 1 0 0.75;320 C5 1 0 0.75;321 G5 1 0 0.75;323 B5 1 0 0.75;324 C6 1 0 0.75;326 A5 1 0 0.75;327 B5 1 0 0.75;329 A5 1 0 0.75;331 E5 1 0 0.75;332 F5 1 0 0.75;333 D5 1 0 0.75;336 C6 1 0 0.75;337 A5 1 0 0.75;339 E5 1 0 0.75;342 E5 1 0 0.75;344 F5 1 0 0.75;345 C6 1 0 0.75;347 C6 1 0 0.75;348 F5 1 0 0.75;352 G5 1 0 0.75;353 F6 1 0 0.75;355 F6 1 0 0.75;356 F6 1 0 0.75;357 E6 1 0 0.75;359 D6 1 0 0.75;360 C6 1 0 0.75;361 A5 1 0 0.75;363 F5 1 0 0.75;364 E5 1 0 0.75;368 C6 1 0 0.75;369 A5 1 0 0.75;371 E5 1 0 0.75;374 E5 1 0 0.75;376 F5 1 0 0.75;377 C6 1 0 0.75;379 C6 1 0 0.75;380 F5 1 0 0.75;0 D3 1 0 0.75;1 D3 1 0 0.75;3 D3 1 0 0.75;5 D3 1 0 0.75;6 D3 1 0 0.75;8 G3 1 0 0.75;12 G3 1 0 0.75;16 G3 1 0 0.75;19 E3 1 0 0.75;22 C3 1 0 0.75;25 F3 1 0 0.75;27 G3 1 0 0.75;29 F#3 1 0 0.75;30 F3 1 0 0.75;32 E3 1 0 0.75;33 C4 1 0 0.75;35 E4 1 0 0.75;36 F4 1 0 0.75;38 D4 1 0 0.75;39 E4 1 0 0.75;41 C4 1 0 0.75;43 A3 1 0 0.75;44 B3 1 0 0.75;45 G3 1 0 0.75;48 G3 1 0 0.75;51 E3 1 0 0.75;54 C3 1 0 0.75;57 F3 1 0 0.75;59 G3 1 0 0.75;61 F#3 1 0 0.75;62 F3 1 0 0.75;64 E3 1 0 0.75;65 C4 1 0 0.75;67 E4 1 0 0.75;68 F4 1 0 0.75;70 D4 1 0 0.75;71 E4 1 0 0.75;73 C4 1 0 0.75;75 A3 1 0 0.75;76 B3 1 0 0.75;77 G3 1 0 0.75;80 C3 1 0 0.75;83 G3 1 0 0.75;86 C4 1 0 0.75;88 F3 1 0 0.75;91 C4 1 0 0.75;92 C4 1 0 0.75;94 F3 1 0 0.75;96 C3 1 0 0.75;99 E3 1 0 0.75;102 G3 1 0 0.75;103 C4 1 0 0.75;105 F3 1 0 0.75;107 F3 1 0 0.75;108 F3 1 0 0.75;110 G3 1 0 0.75;112 C3 1 0 0.75;115 G3 1 0 0.75;118 C4 1 0 0.75;120 F3 1 0 0.75;123 C4 1 0 0.75;124 C4 1 0 0.75;126 F3 1 0 0.75;128 C3 1 0 0.75;130 G#3 1 0 0.75;133 A#3 1 0 0.75;136 C4 1 0 0.75;139 G3 1 0 0.75;140 G3 1 0 0.75;142 C3 1 0 0.75;144 C3 1 0 0.75;147 G3 1 0 0.75;150 C4 1 0 0.75;152 F3 1 0 0.75;155 C4 1 0 0.75;156 C4 1 0 0.75;158 F3 1 0 0.75;160 C3 1 0 0.75;163 E3 1 0 0.75;166 G3 1 0 0.75;167 C4 1 0 0.75;169 F3 1 0 0.75;171 F3 1 0 0.75;172 F3 1 0 0.75;174 G3 1 0 0.75;176 C3 1 0 0.75;179 G3 1 0 0.75;182 C4 1 0 0.75;184 F3 1 0 0.75;187 C4 1 0 0.75;188 C4 1 0 0.75;190 F3 1 0 0.75;192 C3 1 0 0.75;194 G#3 1 0 0.75;197 A#3 1 0 0.75;200 C4 1 0 0.75;203 G3 1 0 0.75;204 G3 1 0 0.75;206 C3 1 0 0.75;208 G#2 1 0 0.75;211 D#3 1 0 0.75;214 G#3 1 0 0.75;216 G3 1 0 0.75;219 C3 1 0 0.75;222 G2 1 0 0.75;224 G#2 1 0 0.75;227 D#3 1 0 0.75;230 G#3 1 0 0.75;232 G3 1 0 0.75;235 C3 1 0 0.75;238 G2 1 0 0.75;240 G#2 1 0 0.75;243 D#3 1 0 0.75;246 G#3 1 0 0.75;248 G3 1 0 0.75;251 C3 1 0 0.75;254 G2 1 0 0.75;256 D3 1 0 0.75;257 D3 1 0 0.75;259 D3 1 0 0.75;261 D3 1 0 0.75;262 D3 1 0 0.75;264 G3 1 0 0.75;268 G3 1 0 0.75;272 G3 1 0 0.75;275 E3 1 0 0.75;278 C3 1 0 0.75;281 F3 1 0 0.75;283 G3 1 0 0.75;285 F#3 1 0 0.75;286 F3 1 0 0.75;288 E3 1 0 0.75;289 C4 1 0 0.75;291 E4 1 0 0.75;292 F4 1 0 0.75;294 D4 1 0 0.75;295 E4 1 0 0.75;297 C4 1 0 0.75;299 A3 1 0 0.75;300 B3 1 0 0.75;301 G3 1 0 0.75;304 G3 1 0 0.75;307 E3 1 0 0.75;310 C3 1 0 0.75;313 F3 1 0 0.75;315 G3 1 0 0.75;317 F#3 1 0 0.75;318 F3 1 0 0.75;320 E3 1 0 0.75;321 C4 1 0 0.75;323 E4 1 0 0.75;324 F4 1 0 0.75;326 D4 1 0 0.75;327 E4 1 0 0.75;329 C4 1 0 0.75;331 A3 1 0 0.75;332 B3 1 0 0.75;333 G3 1 0 0.75;336 C3 1 0 0.75;339 F#3 1 0 0.75;340 G3 1 0 0.75;342 C4 1 0 0.75;344 F3 1 0 0.75;346 F3 1 0 0.75;348 C4 1 0 0.75;349 C4 1 0 0.75;350 F3 1 0 0.75;352 D3 1 0 0.75;355 F3 1 0 0.75;356 G3 1 0 0.75;358 B3 1 0 0.75;360 G3 1 0 0.75;362 G3 1 0 0.75;364 C4 1 0 0.75;365 C4 1 0 0.75;366 G3 1 0 0.75;368 C3 1 0 0.75;371 F#3 1 0 0.75;372 G3 1 0 0.75;374 C4 1 0 0.75;376 F3 1 0 0.75;378 F3 1 0 0.75;380 C4 1 0 0.75;381 C4 1 0 0.75;382 F3 1 0 0.75"
mario_song = music(song, pins=[Pin(23)])

song_1 = '0 A#4 1 1;2 F5 1 1;4 D#5 1 1;8 D5 1 1;11 D5 1 1;6 A#4 1 1;14 D#5 1 1'          
end_song = music(song_1, pins=[Pin(23)])
