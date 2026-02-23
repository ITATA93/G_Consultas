# SQLUser.AR_PatBillICD

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ICD_ParRef | bigint | PK |  | NO | AR_PatientBill Parent Reference |
| ICD_Childsub | double |  |  | NO | Childsub |
| ICD_ICD_DR | bigint |  | FK | SI | Des Ref to MRCID |
| ICD_MRDiagnos_DR | varchar |  | FK | SI | Des Ref to MRDiagnos |
| ICD_RowId | varchar |  |  | NO | - |
| Q01Q1 | - |  |  | SI | Fecha de Ingreso |
| Q01Q2 | - |  |  | SI | Hora de Ingreso |
| Q01Q3 | - |  |  | SI | Tipo de Marca |
| Q01Q4 | - |  |  | SI | Estado |
| Q01Q5 | - |  |  | SI | Comentario |
| Q01Q6 | - |  |  | SI | Usuario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*