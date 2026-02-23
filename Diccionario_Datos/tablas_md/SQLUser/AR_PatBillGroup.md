# SQLUser.AR_PatBillGroup

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BGRP_ParRef | bigint | PK |  | NO | AR_PatientBill Parent Reference |
| BGRP_AAServiceTotal | double |  |  | SI | Authorised Allowed Service Total |
| BGRP_AATotal | double |  |  | SI | Author Allowed Total |
| BGRP_ADServiceTotal | double |  |  | SI | Authorised Disalllowed Service Total |
| BGRP_ADTotal | double |  |  | SI | Author Disallowed Total |
| BGRP_BillGroup_DR | varchar |  | FK | NO | Des Ref to BillSubGroup |
| BGRP_Childsub | double |  |  | NO | Childsub |
| BGRP_RowId | varchar |  |  | NO | - |
| BGRP_SpecSurcharge | double |  |  | SI | Specialist Surcharge |
| ChildQ10DR | - |  |  | SI | Child Reference: Drenajes |
| Q08Q1 | - |  |  | SI | Tipo Dispositivo |
| Q08Q10 | - |  |  | SI | ¿Es Necesario el DI? |
| Q08Q2 | - |  |  | SI | Actividad |
| Q08Q3 | - |  |  | SI | Tamaño |
| Q08Q4 | - |  |  | SI | Acceso |
| Q08Q5 | - |  |  | SI | Ubicación |
| Q08Q6 | - |  |  | SI | Confirmación Ubicación |
| Q08Q7 | - |  |  | SI | Estado |
| Q08Q8 | - |  |  | SI | Descripción Contenido |
| Q08Q9 | - |  |  | SI | N° Días Dispositivo GI |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*