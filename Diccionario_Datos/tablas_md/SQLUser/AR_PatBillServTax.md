# SQLUser.AR_PatBillServTax

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ST_ParRef | bigint | PK |  | NO | AR_PatientBill Parent Reference |
| ChildQ04DR | - |  |  | SI | Child Reference: Contención Farmacológica |
| Q23Q1 | - |  |  | SI | Fecha Control |
| Q23Q10 | - |  |  | SI | Nombre Profesional |
| Q23Q2 | - |  |  | SI | Hora Control |
| Q23Q3 | - |  |  | SI | Tipo Contención |
| Q23Q4 | - |  |  | SI | Estado Contención |
| Q23Q5 | - |  |  | SI | Estado Fijación |
| Q23Q6 | - |  |  | SI | Estado Paciente |
| Q23Q7 | - |  |  | SI | Perfusión PCTE |
| Q23Q8 | - |  |  | SI | Barandas en Alto |
| Q23Q9 | - |  |  | SI | Indicación de Contención por Médico en Ficha |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| ST_BaseAmount | double |  |  | SI | Base Amount |
| ST_Childsub | double |  |  | NO | Childsub |
| ST_RowId | varchar |  |  | NO | - |
| ST_ServTax_DR | bigint |  | FK | SI | Des Ref ServTax |
| ST_TaxRate | double |  |  | SI | Tax Rate |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*