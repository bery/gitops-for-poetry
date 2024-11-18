{{/*
Generate the name of the app based on the chart name and release name.
*/}}
{{- define "python-poetry-app.name" -}}
{{- .Chart.Name -}}
{{- end -}}

{{/*
Generate the full name for the application, typically the chart name and release name.
*/}}
{{- define "python-poetry-app.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Generate the application label.
*/}}
{{- define "python-poetry-app.labels" -}}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version }}
app.kubernetes.io/name: {{ include "python-poetry-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion }}
app.kubernetes.io/managed-by: Helm
{{- end -}}
