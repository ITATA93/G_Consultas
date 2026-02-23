# questionnaire.QCLXXMDIQQ01

> Mantención Dispositivos Invasivos : Vía Venosa Periférica

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Mantención Dispositivos Invasivos : Vía Venosa Periférica

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q01Q1 | varchar |  |  | SI | Tipo VVP |
| Q01Q10 | varchar |  |  | SI | ¿Es necesario el DI?&nbsp; |
| Q01Q2 | varchar |  |  | SI | Ubicación |
| Q01Q3 | varchar |  |  | SI | Actividad |
| Q01Q4 | varchar |  |  | SI | Tamaño Catéter |
| Q01Q5 | varchar |  |  | SI | N° Días VVP |
| Q01Q6 | varchar |  |  | SI | Permeabilidad |
| Q01Q7 | varchar |  |  | SI | Caracteristicas Sitio de Inserción |
| Q01Q8 | varchar |  |  | SI | Estado/Caracterísicas Cobertura |
| Q01Q9 | varchar |  |  | SI | Cuidados VVP |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*