# SQLUser.CF_CT

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCF_RowId1 | double | PK |  | NO | - |
| CTCF_CTCUR_DR | bigint |  | FK | SI | Des Ref to CTCUR (Base Currency) |
| CTCF_ChequeDate | varchar |  |  | SI | Display Cheque Date |
| CTCF_Description | varchar |  |  | SI | Description |
| CTCF_MultipleCurr | varchar |  |  | SI | Allow Multiple Currency |
| CTCF_PayMode | bigint |  |  | SI | Des Ref CTPayMode |
| CTCF_RowId | double |  |  | NO | CTCF Row ID |
| CTCF_TempDir | varchar |  |  | SI | Working temp. Directory for write print file |
| CTCF_UpdateDate | date |  |  | SI | Last Update Date |
| CTCF_UpdateTime | time |  |  | SI | Last Update Time |
| CTCF_UpdateUser_DR | bigint |  | FK | SI | Last Update User |
| ChildQ06DR | - |  |  | SI | Child Reference: TERAPIA OCUPACIONAL |
| Q05Q1 | - |  |  | SI | Objetivos |
| Q05Q2 | - |  |  | SI | Estrategias o Actividades |
| Q05Q3 | - |  |  | SI | Responsables |
| Q05Q4 | - |  |  | SI | Plazo |
| Q05Q5 | - |  |  | SI | Resultados |
| Q05Q6 | - |  |  | SI | Logros |
| Q05Q7 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*