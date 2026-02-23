# SQLUser.IKTestDocument

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AdmissionDate | date |  |  | SI | | 6 |
| AdmissionTime | time |  |  | SI | | 6 |
| Diagnosis | varchar |  |  | SI | | 7 |
| DocumentContent | longvarchar |  |  | SI | - |
| DocumentId | varchar |  |  | SI | - |
| DocumentStatus | varchar |  |  | SI | | 8 |
| DocumentType | varchar |  |  | SI | | 9 |
| HospitalCode | varchar |  |  | SI | | 2 |
| Num1 | varchar |  |  | SI | The following are derived from the document header... |
| Num2 | varchar |  |  | SI | | 3 |
| Num3 | varchar |  |  | SI | | 5 |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*