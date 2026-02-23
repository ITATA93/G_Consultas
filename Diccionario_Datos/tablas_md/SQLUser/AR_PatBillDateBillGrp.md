# SQLUser.AR_PatBillDateBillGrp

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BGRP_ParRef | varchar | PK |  | NO | AR_PatBillDate Parent Reference |
| BGRP_AAServiceTotal | double |  |  | SI | Author Allowed Service Total |
| BGRP_AATotal | double |  |  | SI | Auth Allow Total |
| BGRP_ADServiceTotal | double |  |  | SI | Author Disallow Service Total |
| BGRP_ADTotal | double |  |  | SI | Author Disallow Total |
| BGRP_Childsub | double |  |  | NO | Childsub |
| BGRP_RowId | varchar |  |  | NO | - |
| BGRP_SpecSurcharge | double |  |  | SI | Specialist Surcharge |
| ChildQ05DR | - |  |  | SI | Child Reference: Catéteres Arteriales |
| Q02Q1 | - |  |  | SI | Tipo Catéteres |
| Q02Q10 | - |  |  | SI | ¿Es necesario el DI? |
| Q02Q2 | - |  |  | SI | Actividad |
| Q02Q3 | - |  |  | SI | Ubicación |
| Q02Q4 | - |  |  | SI | Tamaño Catéter |
| Q02Q5 | - |  |  | SI | N° Días de Catéter |
| Q02Q6 | - |  |  | SI | Permeabilidad |
| Q02Q7 | - |  |  | SI | Características Sitio de Inserción |
| Q02Q8 | - |  |  | SI | Estado de Cobertura |
| Q02Q9 | - |  |  | SI | Solución Antiséptica |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*