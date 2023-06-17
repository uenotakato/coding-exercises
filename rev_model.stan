data {
  int<lower=0> N_A;  // 商品Aのレビュー数
  int<lower=0> N_B;  // 商品Bのレビュー数
  real<lower=0, upper=5> mu_A;  // 商品Aのレビュー平均
  real<lower=0, upper=5> mu_B;  // 商品Bのレビュー平均
}

parameters {
  real<lower=0, upper=5> mu_A_hat;  // 商品Aの信頼性の推定値
  real<lower=0, upper=5> mu_B_hat;  // 商品Bの信頼性の推定値
}

model {
  mu_A_hat ~ uniform(0, 5);  // 商品Aの信頼性の事前分布
  mu_B_hat ~ uniform(0, 5);  // 商品Bの信頼性の事前分布
  N_A ~ normal(mu_A_hat, 1);  // 商品Aのレビュー数の尤度関数
  N_B ~ normal(mu_B_hat, 1);  // 商品Bのレビュー数の尤度関数
}
