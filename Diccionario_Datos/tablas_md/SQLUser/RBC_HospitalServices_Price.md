# SQLUser.RBC_HospitalServices_Price

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRICE_ParRef | bigint | PK |  | NO | RBC_HospitalServices Parent Reference |
| PRICE_Childsub | double |  |  | NO | Childsub |
| PRICE_Cost | double |  |  | SI | Cost |
| PRICE_CreatedDate | date |  |  | SI | Created Date |
| PRICE_CreatedTime | time |  |  | SI | Created Time |
| PRICE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PRICE_Currency_DR | bigint |  | FK | SI | Des Ref Currency |
| PRICE_DateFrom | date |  |  | NO | Date From |
| PRICE_DateTo | date |  |  | SI | Date To |
| PRICE_DoctorPerc | double |  |  | SI | Doctor % |
| PRICE_NoOfSlots | double |  |  | SI | No Of Slots |
| PRICE_Price | double |  |  | SI | Price |
| PRICE_RowId | varchar |  |  | NO | - |
| PRICE_Tariff_DR | bigint |  | FK | SI | Des Ref Tariff |
| PRICE_UpdatedDate | date |  |  | SI | Updated Date |
| PRICE_UpdatedTime | time |  |  | SI | Updated Time |
| PRICE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*