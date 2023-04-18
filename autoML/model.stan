data {
  int<lower=0> N;
  int<lower=0> a;
  real<lower=0> prior_a;
  real<lower=0> prior_b;
}

parameters {
  real<lower=0,upper=1> theta;
}

model {
  theta ~ beta(prior_a, prior_b);
  a ~ binomial(N, theta);
}
