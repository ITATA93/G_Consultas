# TC_hmf_Message_HS_Community.TaskItem

**Schema:** TC_hmf_Message_HS_Community
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Description | varchar |  |  | SI | Description of the task or task item |
| DocumentFileType | varchar |  |  | SI | This field indicates the format or type of the doc... |
| DocumentLink | varchar |  |  | SI | Document Type Specific Properties
The link to acc... |
| DocumentStream | varchar |  |  | SI | This is a string field that holds the base64 encod... |
| DocumentType | varchar |  |  | SI | This field represents the type of the document. It... |
| ExternalTaskItemID | varchar |  |  | NO | Id of current task item in TrakCare |
| Name | varchar |  |  | NO | Name of the task or task item |
| QuestionnaireCode | varchar |  |  | SI | Questionnaire Type properties
The string that rep... |
| QuestionnaireID | integer |  |  | SI | The integer that represents the "instance" of a Qu... |
| Status | varchar |  |  | NO | Status of the task item. Statuses include: ToDo, R... |
| Type | varchar |  |  | NO | Type of the task item. Current task item types inc... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*