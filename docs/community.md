---
id: community 
title: Join Litmus Community
sidebar_label: Community 
---
------

Litmus community is a subset of the larger Kubernetes community. Have a question? Want to stay in touch with the happenings on Chaos Engineering on Kubernetes? Join `#litmus` channel on Kubernetes Slack. 

<br><br>

<a href="https://kubernetes.slack.com/messages/CNXNB0ZTN" target="_blank"><img src="/docs/assets/join-community.png" width="400"></a>

<br>	

<br>

<hr>

<br>

<br>

[embedmd]:# (https://litmuschaos.github.io/litmus/litmus-admin-rbac.yaml)
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: litmus-admin
  namespace: litmus
  labels:
    name: litmus-admin
---
# Source: openebs/templates/clusterrole.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: litmus-admin
  labels:
    name: litmus-admin
rules:
- apiGroups: ["","apps","batch","extensions","litmuschaos.io"]
  resources: ["pods","pods/exec","pods/eviction","jobs","daemonsets","events","chaosresults","chaosengines"]
  verbs: ["create","delete","get","list","patch","update", "deletecollection"]
- apiGroups: ["","apps","litmuschaos.io"]
  resources: ["configmaps","secrets","services","chaosexperiments","pods/log","replicasets","deployments","statefulsets","services"]
  verbs: ["get","list","patch","update"]
- apiGroups: [""]
  resources: ["nodes"]
  verbs: ["get","list","patch","update"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: litmus-admin
  labels:
    name: litmus-admin
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: litmus-admin
subjects:
- kind: ServiceAccount
  name: litmus-admin
  namespace: litmus

```
