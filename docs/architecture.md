---
id: architecture 
title: Litmus Architecture
sidebar_label: Architecture 
---
<hr>

<img src="/docs/assets/litmus-schematic.png" width="800">

**Chaos-Operator**

Chaos-Operator watches for the ChaosEngine CR and executes the Chaos-Experiments mentioned in the CR. Chaos-Operator is namespace scoped. By default, it runs in `litmus` namespace. Once the experiment is completed, chaos-operator invokes chaos-exporter to export chaos metrics to a Prometheus database. 

**Chaos-CRDs**

During installation, the following three CRDs are installed on the Kubernetes cluster. 

`chaosengines.litmuschaos.io`

`chaosexperiments.litmuschaos.io`

`chaosresults.litmuschaos.io`


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

**Chaos-Experiments**

Chaos Experiment is a CR and are available as YAML files on <a href=" https://hub.litmuschaos.io" target="_blank">Chaos Hub</a>. For more details visit Chaos Hub [documentation](chaoshub.md).



**Chaos-Engine**

ChaosEngine CR links application to experiments. User has to create ChaosEngine YAML by specifying the application label and experiments and create the CR. The CR is watched by Chaos-Operator and chaos-experiments are executed on a given application. 



**Chaos-Exporter**

Optionally metrics can be exported to a Prometheus database. Chaos-Exporter implements the  Prometheus metrics endpoint. 



<br>

<br>

<hr>

<br>

<br>


