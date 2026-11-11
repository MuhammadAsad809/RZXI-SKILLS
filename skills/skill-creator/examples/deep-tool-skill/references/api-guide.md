# API & Metric Guide — Deep Tool Skill

`[DARKCODE::EXAMPLE::API_GUIDE]`

## Entropy Calculation Metric

Shannon entropy is defined as:

$$H(X) = -\sum_{i=1}^{n} P(x_i) \log_2 P(x_i)$$

Where:
- $n = 256$ for byte frequencies $[0x00, 0xFF]$.
- $P(x_i)$ is the empirical probability of byte $x_i$ occurring in the target slice.

### Interpretation Thresholds:
- **$0.0 - 2.5$**: Highly uniform / sparse data (e.g. zero-padded buffers).
- **$3.0 - 5.5$**: Standard English ASCII text or uncompressed machine code.
- **$6.0 - 7.0$**: Compressed native executable text, dense object files.
- **$> 7.2$**: Encrypted ciphertext, high-entropy packers (UPX, VMProtect, Themida).
