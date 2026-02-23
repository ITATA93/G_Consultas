# SQLUser.LBC_RapidRequestForm

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCRRF_RowID | bigint | PK |  | NO | - |
| ChildQ161DR | - |  |  | SI | Child Reference: Requisitos de vencimientos |
| LBCRRF_Code | varchar |  |  | NO | Code	 |
| LBCRRF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCRRF_CreatedDate | date |  |  | SI | Created Date |
| LBCRRF_CreatedTime | time |  |  | SI | Created Time |
| LBCRRF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCRRF_DateFrom | date |  |  | SI | Effective date for the record |
| LBCRRF_DateTo | date |  |  | SI | Last day the record is active  |
| LBCRRF_Desc | varchar |  |  | NO | Description  |
| LBCRRF_Owner | varchar |  |  | SI | Owner |
| LBCRRF_UpdatedDate | date |  |  | SI | Updated Date |
| LBCRRF_UpdatedTime | time |  |  | SI | Updated Time |
| LBCRRF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q160Q1 | - |  |  | SI | Acción |
| Q160Q2 | - |  |  | SI | Tipo de Dispositivo |
| Q160Q3 | - |  |  | SI | Medida |
| Q160Q4 | - |  |  | SI | Ubicación |
| Q160Q5 | - |  |  | SI | Número de Intentos de Instalación |
| Q160Q6 | - |  |  | SI | Médico Responsable Indicación |
| Q160Q7 | - |  |  | SI | Responsable Instalación/Retiro |
| Q160Q8 | - |  |  | SI | Fecha |
| Q160Q9 | - |  |  | SI | Hora |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*