# SQLUser.RBC_EquipmentProcExclusion

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EQEX_ParRef | bigint | PK |  | NO | RBAS Par Ref |
| EQEX_Childsub | double |  |  | NO | Childsub |
| EQEX_DateFrom | date |  |  | SI | Date From |
| EQEX_DateTo | date |  |  | SI | Date To |
| EQEX_Operation_DR | bigint |  | FK | SI | Excluded Operation |
| EQEX_RowId | varchar |  |  | NO | - |
| EQEX_StatePPP_DR | bigint |  | FK | SI | Excluded Procedure |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*