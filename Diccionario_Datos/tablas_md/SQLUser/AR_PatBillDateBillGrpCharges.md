# SQLUser.AR_PatBillDateBillGrpCharges

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | varchar | PK |  | NO | AR_PatientBillDateBillGrp Parent Reference |
| ChildQ06DR | - |  |  | SI | Child Reference: Dispositivos Vías Urinarias |
| ITM_ARPBLItem_DR | varchar |  | FK | SI | Des Ref ARPBLItem |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_RowId | varchar |  |  | NO | - |
| Q05Q1 | - |  |  | SI | N° |
| Q05Q10 | - |  |  | SI | Comentarios |
| Q05Q2 | - |  |  | SI | Actividad |
| Q05Q3 | - |  |  | SI | Ubicación |
| Q05Q4 | - |  |  | SI | Tamaño Línea Arterial |
| Q05Q5 | - |  |  | SI | N° Días Línea Arterial |
| Q05Q6 | - |  |  | SI | Permeabilidad |
| Q05Q7 | - |  |  | SI | Sitio Inserción |
| Q05Q8 | - |  |  | SI | Estado Cobertura |
| Q05Q9 | - |  |  | SI | ¿Es necesario el DI? |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*